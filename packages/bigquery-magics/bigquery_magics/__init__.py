# Copyright 2020 Google LLC
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

import bigquery_magics.config
import bigquery_magics.version

context = bigquery_magics.config.context
__version__ = bigquery_magics.version.__version__

# Whether the magics has already been reigstered by some other packages.
is_registered = False


def load_ipython_extension(ipython):
    """Called by IPython when this module is loaded as an IPython extension."""
    # Import here to avoid circular imports.
    from bigquery_magics.bigquery import _cell_magic

    ipython.register_magic_function(
        _cell_magic, magic_kind="cell", magic_name="bigquery"
    )

    global is_registered
    is_registered = True


def unload_ipython_extension(ipython):
    global is_registered
    is_registered = False


__all__ = (
    # For backwards compatibility we need to make the context available in
    # the path google.cloud.bigquery.magics.context.
    "context",
    "__version__",
    "load_ipython_extension",
    "unload_ipython_extension",
    "is_registered",
)
