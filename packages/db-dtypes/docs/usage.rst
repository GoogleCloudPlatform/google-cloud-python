Using the db-dtypes package
---------------------------

Importing the :mod:`db_dtypes` module registers the extension dtypes for use
in pandas.

Construct a date :class:`~pandas.Series` with strings in ``YYYY-MM-DD`` format
or :class:`datetime.date` objects.

.. code-block:: python

   import datetime
   import pandas as pd
   import db_dtypes  # noqa import to register dtypes

   dates = pd.Series([datetime.date(2021, 9, 17), "2021-9-18"], dtype="dbdate")

Working with dates
^^^^^^^^^^^^^^^^^^

Convert a date :class:`~pandas.Series` to a ``datetime64`` Series with
:meth:`~pandas.Series.astype`. The resulting values use midnight as the
time part.

.. code-block:: python

   datetimes = dates.astype("datetime64")

Just like ``datetime64`` values, date values can be subtracted. This is
equivalent to first converting to ``datetime64`` and then subtracting.

.. code-block:: python

   dates2 = pd.Series(["2021-1-1", "2021-1-2"], dtype="dbdate")
   diffs = dates - dates2

Just like ``datetime64`` values, :class:`~pandas.tseries.offsets.DateOffset`
values can be added to them.

.. code-block:: python

   do = pd.DateOffset(days=1)
   after = dates + do
   before = dates - do


Working with times
^^^^^^^^^^^^^^^^^^

Construct a time :class:`~pandas.Series` with strings in ``HH:MM:SS.fraction``
24-hour format or :class:`datetime.time` objects.

.. code-block:: python

   times = pd.Series([datetime.time(1, 2, 3, 456789), "12:00:00.6"], dtype="dbtime")

Convert a time :class:`~pandas.Series` to a ``timedelta64`` Series with
:meth:`~pandas.Series.astype`.

.. code-block:: python

   timedeltas = times.astype("timedelta64")


Combining dates and times
^^^^^^^^^^^^^^^^^^^^^^^^^

Combine a date :class:`~pandas.Series` with a time :class:`~pandas.Series` to
create a ``datetime64`` :class:`~pandas.Series`.

.. code-block:: python

   combined = dates + times
