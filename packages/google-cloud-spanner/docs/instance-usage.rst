Instance Admin Usage
====================

After creating a :class:`~google.cloud.spanner_v1.client.Client`, you can
interact with individual instances for a project.

Instance Configurations
-----------------------

Each instance within a project maps to a named "instance configuration",
specifying the location and other parameters for a set of instances.  These
configurations are defined by the server, and cannot be changed.

To iterate over all instance configurations available to your project, use the
:meth:`~google.cloud.spanner_v1.client.Client.list_instance_configs`
method of the client:

.. code:: python

    for config in client.list_instance_configs():
        # `config` is an instance of `InstanceConfig`


To fetch a single instance configuration, use the
:meth:`~google.cloud.spanner_v1.client.Client.get_instance_configuration`
method of the client:

.. code:: python

    config = client.get_instance_configuration('config-name')

Each of these methods provide
:class:`~.spanner_admin_instance_v1.types.InstanceConfig` objects.


List Instances
--------------

If you want a comprehensive list of all existing instances, iterate over the
:meth:`~google.cloud.spanner_v1.client.Client.list_instances` method of
the client:

.. code:: python

    for instance in client.list_instances():
        # `instance` is an instance of `Instance`

This iterator yields :class:`~.spanner_admin_instance_v1.types.Instance`
objects.


Instance Factory
----------------

To create a :class:`~google.cloud.spanner_v1.instance.Instance` object:

.. code:: python

    config = configs[0]
    instance = client.instance(instance_id,
                               configuration_name=config.name,
                               node_count=10,
                               display_name='My Instance')

- ``configuration_name`` is the name of the instance configuration to which the
  instance will be bound.  It must be one of the names configured for your
  project, discoverable via
  :meth:`~google.cloud.spanner_v1.client.Client.list_instance_configs`.

- ``node_count`` is a postitive integral count of the number of nodes used
  by the instance.  More nodes allows for higher performance, but at a higher
  billing cost.

- ``display_name`` is optional. When not provided, ``display_name`` defaults
  to the ``instance_id`` value.

You can also use :meth:`Client.instance` to create a local wrapper for
an instance that has already been created:

.. code:: python

    instance = client.instance(existing_instance_id)
    instance.reload()


Create a new Instance
---------------------

After creating the instance object, use its
:meth:`~google.cloud.spanner_v1.instance.Instance.create` method to
trigger its creation on the server:

.. code:: python

    instance.display_name = 'My very own instance'
    operation = instance.create()

.. note::

    Creating an instance triggers a "long-running operation" and
    returns an :class:`google.cloud.spanner_v1.instance.Operation`
    object.  See :ref:`check-on-current-instance-operation` for polling
    to find out if the operation is completed.


Refresh metadata for an existing Instance
-----------------------------------------

After creating the instance object, reload its server-side configuration
using its :meth:`~google.cloud.spanner_v1.instance.Instance.reload` method:

.. code:: python

    instance.reload()

This will load ``display_name``, ``config_name``, and ``node_count``
for the existing ``instance`` object from the back-end.


Update an existing Instance
---------------------------

After creating the instance object, you can update its metadata via
its :meth:`~google.cloud.spanner_v1.instance.Instance.update` method:

.. code:: python

    client.display_name = 'New display_name'
    operation = instance.update()

.. note::

    Update an instance triggers a "long-running operation" and
    returns a :class:`google.cloud.spanner_v1.instance.Operation`
    object.  See :ref:`check-on-current-instance-operation` for polling
    to find out if the operation is completed.


Delete an existing Instance
---------------------------

Delete an instance using its
:meth:`~google.cloud.spanner_v1.instance.Instance.delete` method:

.. code:: python

    instance.delete()


.. _check-on-current-instance-operation:

Resolve Current Instance Operation
----------------------------------

The :meth:`~google.cloud.spanner_v1.instance.Instance.create` and
:meth:`~google.cloud.spanner_v1.instance.Instance.update` methods of instance
object trigger long-running operations on the server, and return instances
of the :class:`~google.cloud.spanner_v1.instance.Operation` class.

If you want to block on the completion of those operations, use the
``result`` method on the returned objects:

.. code:: python

    >>> operation = instance.create()
    >>> result = operation.result()

This method will raise an exception if the operation fails.


Next Step
---------

Now we go down the hierarchy from
:class:`~google.cloud.spanner_v1.instance.Instance` to a
:class:`~google.cloud.spanner_v1.database.Database`.

Next, learn about the :doc:`database-usage`.


.. _Instance Admin API: https://cloud.google.com/spanner/reference/rpc/google.spanner.admin.instance.v1
