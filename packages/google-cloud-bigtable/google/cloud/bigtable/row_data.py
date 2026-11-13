# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Container for Google Cloud Bigtable Cells and Streaming Row Contents."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generator

from google.api_core import exceptions, retry

from google.cloud.bigtable.row import Cell, InvalidChunk, PartialRowData

if TYPE_CHECKING:
    from google.cloud.bigtable.data.row import Row

# Some classes need to be re-exported here to keep backwards
# compatibility. Those classes were moved to row_merger, but we dont want to
# break enduser's imports. This hack, ensures they don't get marked as unused.
_ = (Cell, InvalidChunk, PartialRowData)


class PartialCellData(object):  # pragma: NO COVER
    """This class is no longer used and will be removed in the future"""

    def __init__(
        self, row_key, family_name, qualifier, timestamp_micros, labels=(), value=b""
    ):
        self.row_key = row_key
        self.family_name = family_name
        self.qualifier = qualifier
        self.timestamp_micros = timestamp_micros
        self.labels = labels
        self.value = value

    def append_value(self, value):
        self.value += value


class InvalidReadRowsResponse(RuntimeError):
    """Exception raised to invalid response data from back-end."""


class InvalidRetryRequest(RuntimeError):
    """Exception raised when retry request is invalid."""


DEFAULT_RETRY_READ_ROWS = retry.Retry(
    initial=1.0,
    maximum=15.0,
    multiplier=2.0,
    deadline=60.0,  # 60 seconds
)
"""The default retry strategy to be used on retry-able errors.

Used by
:meth:`~google.cloud.bigtable.row_data.PartialRowsData._read_next_response`.
"""


class PartialRowsData(object):
    """Convenience wrapper for consuming a ``ReadRows`` streaming response.

    This class will be returned by the ``read_rows`` method, and should not
    be constructed manually.

    :type read_method: :class:`client._table_data_client.read_rows`
    :param read_method: ``ReadRows`` method.

    :type generator: :class:`Iterable[Row]`
    :param generator: The `Row` iterator from :meth:`Table.read_rows`.
    """

    def __init__(
        self,
        *args: Any,
        generator: Generator[Row, Any, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        self._generator: Generator[Row, Any, Any]
        if generator is not None and not args and not kwargs:
            self._generator = generator
        else:
            import warnings

            warnings.warn(
                "Direct instantiation of `PartialRowsData` is deprecated "
                "and will be removed in a future release. `PartialRowsData` should only be obtained "
                "by calling `Table.read_rows()`. An empty stream has been initialized.",
                DeprecationWarning,
                stacklevel=2,
            )
            self._generator = (x for x in ())

        self.rows: dict[bytes, PartialRowData] = {}

    @classmethod
    def _from_generator(cls, generator: Generator[Row, Any, Any]) -> PartialRowsData:
        """Internal constructor for Table.read_rows."""
        return cls(generator=generator)

    @property
    def state(self):
        import warnings

        warnings.warn(
            "The `state` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def last_scanned_row_key(self):
        import warnings

        warnings.warn(
            "The `last_scanned_row_key` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def read_method(self):
        import warnings

        warnings.warn(
            "The `read_method` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def request(self):
        import warnings

        warnings.warn(
            "The `request` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def retry(self):
        import warnings

        warnings.warn(
            "The `retry` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def response_iterator(self):
        import warnings

        warnings.warn(
            "The `response_iterator` attribute on `PartialRowsData` is deprecated "
            "and will return None.",
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    def cancel(self):
        """Cancels the iterator, closing the stream."""
        self._generator.close()

    def consume_all(self, max_loops=None):
        """Consume the streamed responses until there are no more.

        .. warning::
           This method will be removed in future releases.  Please use this
           class as a generator instead.

        :type max_loops: int
        :param max_loops: (Deprecated). Maximum number of times to try to consume
                          an additional ``ReadRowsResponse``. This parameter is
                          deprecated and is only kept for backwards compatibility.
        """
        for row in self:
            self.rows[row.row_key] = row

    def __iter__(self):
        """Consume the ``Row`` s from the stream.
        Convert them to ``PartialRowData`` and yield each to the reader.
        """
        try:
            for row in self._generator:
                yield PartialRowData._from_data_client_row(row)

        # Any exception from the generator should cancel the iterator. A
        # timeout, defined by catching a DeadlineExceeded, should be reraised
        # as a RetryError instead.
        except exceptions.DeadlineExceeded as e:
            self.cancel()
            raise exceptions.RetryError(e.message, e.__cause__)
        except Exception as e:
            self.cancel()
            raise e
