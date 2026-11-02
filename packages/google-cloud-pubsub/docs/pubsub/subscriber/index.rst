Subscribing to Messages
=======================

Subscribing to messages is handled through the
:class:`~.pubsub_v1.subscriber.client.Client` class (aliased as
``google.cloud.pubsub.SubscriberClient``). This class provides a
:meth:`~.pubsub_v1.subscriber.client.Client.subscribe` method to
attach to subscriptions on existing topics.

Instantiating a subscriber client is straightforward:

.. code-block:: python

    from google.cloud import pubsub

    with pubsub.SubscriberClient() as subscriber:
        # ...

Creating a Subscription
-----------------------

In Pub/Sub, a **subscription** is a discrete pull of messages from a topic.
If multiple clients pull the same subscription, then messages are split
between them. If multiple clients create a subscription each, then each client
will get every message.

.. note::

    Remember that Pub/Sub operates under the principle of "everything at least
    once". Even in the case where multiple clients pull the same subscription,
    *some* redundancy is likely.

Creating a subscription requires that you already know what topic you want
to subscribe to, and it must already exist. Once you have that, it is easy:

.. code-block:: python

    # Substitute PROJECT, SUBSCRIPTION, and TOPIC with appropriate values for
    # your application.

    # from google.cloud import pubsub
    # publisher = pubsub.PublisherClient()

    topic_path = publisher.topic_path(PROJECT, TOPIC)

    with pubsub.SubscriberClient() as subscriber: 
        sub_path = subscriber.subscription_path(PROJECT, SUBSCRIPTION)
        subscriber.create_subscription(request={"name": sub_path, "topic": topic_path})

Once you have created a subscription (or if you already had one), the next
step is to pull data from it.


Pulling a Subscription Synchronously
------------------------------------

To pull the messages synchronously, use the client's
:meth:`~.pubsub_v1.subscriber.client.Client.pull` method.

.. code-block:: python

    # Wrap the following code in `with pubsub.SubscriberClient() as subscriber:`

    # Substitute PROJECT and SUBSCRIPTION with appropriate values for your
    # application.
    subscription_path = subscriber.subscription_path(PROJECT, SUBSCRIPTION)
    response = subscriber.pull(
        request={
            "subscription": subscription_path,
            "max_messages": 5,
        }
    )

    for msg in response.received_messages:
        print("Received message:", msg.message.data)

    ack_ids = [msg.ack_id for msg in response.received_messages]
    subscriber.acknowledge(
        request={
            "subscription": subscription_path,
            "ack_ids": ack_ids,
        }
    )

The method returns a :class:`~.pubsub_v1.types.PullResponse` instance that
contains a list of received :class:`~.pubsub_v1.types.ReceivedMessage`
instances.

If you want to **nack** some of the received messages (see :ref:`explaining-ack` below),
you can use the :meth:`~.pubsub_v1.subscriber.client.Client.modify_ack_deadline`
method and set their acknowledge deadlines to zero. This will cause them to
be dropped by this client and the backend will try to re-deliver them.

.. code-block:: python

    # Wrap the following code in `with pubsub.SubscriberClient() as subscriber:`

    ack_ids = []  # TODO: populate with `ack_ids` of the messages to NACK
    ack_deadline_seconds = 0
    subscriber.modify_ack_deadline(
        request={
            "subscription": subscription_path,
            "ack_ids": ack_ids,
            "ack_deadline_seconds": ack_deadline_seconds,
        }
    )


Pulling a Subscription Asynchronously
-------------------------------------

The subscriber client uses the
:meth:`~.pubsub_v1.subscriber.client.Client.subscribe` method to start a
background thread to receive messages from Pub/Sub and calls a callback with
each message received.

.. code-block:: python

    # Wrap the following code in `with pubsub.SubscriberClient() as subscriber:`

    # Substitute PROJECT and SUBSCRIPTION with appropriate values for your
    # application.
    subscription_path = subscriber.subscription_path(PROJECT, SUBSCRIPTION)
    future = subscriber.subscribe(subscription_path, callback)

This will return a
:class:`~.pubsub_v1.subscriber.futures.StreamingPullFuture`. This future allows
you to control the background thread that is managing the subscription.


Subscription Callbacks
----------------------

Messages received from a subscription are processed asynchronously through
**callbacks**.

The basic idea: Define a function that takes one argument; this argument
will be a :class:`~.pubsub_v1.subscriber.message.Message` instance, which is
a convenience wrapper around the :class:`~.pubsub_v1.types.PubsubMessage`
instance received from the server (and stored under the ``message`` attribute).

This function should do whatever processing is necessary. At the end, the
function should either :meth:`~.pubsub_v1.subscriber.message.Message.ack`
or :meth:`~.pubsub_v1.subscriber.message.Message.nack` the message.

When you call :meth:`~.pubsub_v1.subscriber.client.Client.subscribe`, you
must pass the callback that will be used.

Here is an example:

.. code-block:: python

    # Define the callback.
    # Note that the callback is defined *before* the subscription is opened.
    def callback(message):
        do_something_with(message)  # Replace this with your actual logic.
        message.ack()  # Asynchronously acknowledge the message.

    # Wrap the following code in `with pubsub.SubscriberClient() as subscriber:`
    
    # Substitute PROJECT and SUBSCRIPTION with appropriate values for your
    # application.
    subscription_path = subscriber.subscription_path(PROJECT, SUBSCRIPTION)

    # Open the subscription, passing the callback.
    future = subscriber.subscribe(subscription_path, callback)

The :meth:`~.pubsub_v1.subscriber.client.Client.subscribe` method returns
a :class:`~.pubsub_v1.subscriber.futures.StreamingPullFuture`, which is both
the interface to wait on messages (e.g. block the primary thread) and to
address exceptions.

To block the thread you are in while messages are coming in the stream,
use the :meth:`~.pubsub_v1.subscriber.futures.Future.result` method:

.. code-block:: python

    future.result()

.. note: This will block forever assuming no errors or that ``cancel`` is never
    called.

You can also use this for error handling; any exceptions that crop up on a
thread will be set on the future.

.. code-block:: python

    try:
        future.result()
    except Exception as ex:
        # Close the subscriber if not using a context manager.
        subscriber.close()
        raise

Finally, you can use
:meth:`~.pubsub_v1.subscriber.futures.StreamingPullFuture.cancel` to stop
receiving messages.


.. code-block:: python

    future.cancel()


.. _explaining-ack:

Explaining Ack
--------------

In Pub/Sub, the term **ack** stands for "acknowledge". You should ack a
message when your processing of that message *has completed*. When you ack
a message, you are telling Pub/Sub that you do not need to see it again.

It might be tempting to ack messages immediately on receipt. While there
are valid use cases for this, in general it is unwise. The reason why: If
there is some error or edge case in your processing logic, and processing
of the message fails, you will have already told Pub/Sub that you successfully
processed the message. By contrast, if you ack only upon completion, then
Pub/Sub will eventually re-deliver the unacknowledged message.

It is also possible to **nack** a message, which is the opposite. When you
nack, it tells Pub/Sub that you are unable or unwilling to deal with the
message, and that the service should redeliver it.


API Reference
-------------

.. toctree::
  :maxdepth: 2

  api/client
  api/message
  api/futures
  api/pagers
  api/scheduler
