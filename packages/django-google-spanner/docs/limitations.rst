Current limitations
-------------------

``AutoField`` generates random IDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner doesn't have support for auto-generating primary key values.
Therefore, ``django-google-spanner`` monkey-patches ``AutoField`` to generate a
random UUID4. It generates a default using ``Field``'s ``default`` option which
means ``AutoField``\ s will have a value when a model instance is created. For
example:

::

    >>> ExampleModel()
    >>> ExampleModel.pk
    4229421414948291880

To avoid
`hotspotting <https://cloud.google.com/spanner/docs/schema-design#uuid_primary_key>`__,
these IDs are not monotonically increasing. This means that sorting
models by ID isn't guaranteed to return them in the order in which they
were created.

``ForeignKey`` constraints aren't created (`#313 <https://github.com/googleapis/python-spanner-django/issues/313>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner does not support ``ON DELETE CASCADE`` when creating foreign-key
constraints, so this is not supported in ``django-google-spanner``.


No native support for ``DecimalField``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner's support for `Decimal <https://www.python.org/dev/peps/pep-0327/>`__
types is limited to
`NUMERIC <https://cloud.google.com/spanner/docs/data-types#numeric_types>`__
precision. Higher-precision values can be stored as strings instead.


``Meta.order_with_respect_to`` model option isn't supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature uses a column name that starts with an underscore
(``_order``) which Spanner doesn't allow.

Random ``QuerySet`` ordering isn't supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner does not support it and will throw an exception. For example:

::

    >>> ExampleModel.objects.order_by('?')
    ...
    django.db.utils.ProgrammingError: 400 Function not found: RANDOM ... FROM
    example_model ORDER BY RANDOM() ASC

Schema migrations
~~~~~~~~~~~~~~~~~

There are some limitations on schema changes to consider:

-  No support for renaming tables and columns;
-  A column's type can't be changed;
-  A table's primary key can't be altered.

``DurationField`` arithmetic doesn't work with ``DateField`` values (`#253 <https://github.com/googleapis/python-spanner-django/issues/253>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner requires using different functions for arithmetic depending on
the column type:

-  ``TIMESTAMP`` columns (``DateTimeField``) require ``TIMESTAMP_ADD``
   or ``TIMESTAMP_SUB``
-  ``DATE`` columns (``DateField``) require ``DATE_ADD`` or ``DATE_SUB``

Django does not provide ways to determine which database function to
use. ``DatabaseOperations.combine_duration_expression()`` arbitrarily uses
``TIMESTAMP_ADD`` and ``TIMESTAMP_SUB``. Therefore, if you use a
``DateField`` in a ``DurationField`` expression, you'll likely see an error
such as:

::

    "No matching signature for function TIMESTAMP\_ADD for argument types:
    DATE, INTERVAL INT64 DATE\_TIME\_PART."

Computations that yield FLOAT64 values cannot be assigned to INT64 columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner does not support this (`#331
<https://github.com/googleapis/python-spanner-django/issues/331>`__) and will
throw an error:

::

    >>> ExampleModel.objects.update(integer=F('integer') / 2)
    ...
    django.db.utils.ProgrammingError: 400 Value of type FLOAT64 cannot be
    assigned to integer, which has type INT64 [at 1:46]\nUPDATE
    example_model SET integer = (example_model.integer /...

Addition with null values crash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additions cannot include ``None`` values. For example:

::

    >>> Book.objects.annotate(adjusted_rating=F('rating') + None)
    ...
    google.api_core.exceptions.InvalidArgument: 400 Operands of + cannot be literal
    NULL ...

stddev() and variance() function call with sample population only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spanner supports `stddev()` and `variance()` functions (`link <https://cloud.google.com/spanner/docs/statistical_aggregate_functions>`__).

Django’s Variance and StdDev database functions have 2 modes.
One with full population `STDDEV_POP` and another with sample population `STDDEV_SAMP` and `VAR_SAMP`.
Currently spanner only supports these functions with samples and not the full population `STDDEV_POP`,


Interleaving is not supported currently
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interleaving is a feature that is supported by spanner database `link <https://cloud.google.com/spanner/docs/schema-and-data-model#creating_a_hierarchy_of_interleaved_tables>`_.
But currently django spanner does not support this feature, more details on this is discussed in this `github issue <https://github.com/googleapis/python-spanner-django/issues/618>`_.

Update object by passing primary key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In django3.1 a new feature was introduced, `<instance>._state.adding`, 
this allowed spanner to resolve `this bug <https://code.djangoproject.com/ticket/29260>`_.

But introduced a new issue with spanner django. Calling `instance.save()` an object after setting it's primary key to an existing primary key value,
will cause a `IntegrityError` as follows: `django.db.utils.IntegrityError: (1062, "Duplicate entry ....`

The workaround for this is to update `<instance>._state.adding` to `False`.
Example: 
.. code:: python

    >>> # This test case passes.
    >>> def test_update_primary_with_default(self):
    >>>         obj = PrimaryKeyWithDefault()
    >>>         obj.save()
    >>>         obj_2 = PrimaryKeyWithDefault(uuid=obj.uuid)
    >>>         obj_2._state.adding = False
    >>>         obj_2.save()

    >>> # This test case fails with `IntegrityError`.
    >>> def test_update_primary_with_default(self):
    >>>         obj = PrimaryKeyWithDefault()
    >>>         obj.save()
    >>>         obj_2 = PrimaryKeyWithDefault(uuid=obj.uuid)
    >>>         obj_2.save()

More details about this issue can be tracked `here <https://code.djangoproject.com/ticket/33052>`_. 

Support for query inside JSONfield is currently not there
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have also added support for JSON object storage and retrieval with Django 3.2.x support in v2.2.1b4 release,
but querying inside the JSONfield is not supported in the current `django-google-spanner` release.
This feature is being worked on and can be tracked `here <https://github.com/googleapis/python-spanner-django/issues/716>`_.
