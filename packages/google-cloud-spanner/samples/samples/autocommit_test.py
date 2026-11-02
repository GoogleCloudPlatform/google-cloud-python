# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from google.api_core.exceptions import Aborted
from test_utils.retry import RetryErrors

import autocommit


@RetryErrors(exception=Aborted, max_tries=2)
def test_enable_autocommit_mode(capsys, instance_id, sample_database):
    # Delete table if it exists for retry attempts.
    table = sample_database.table("Singers")
    if table.exists():
        op = sample_database.update_ddl(["DROP TABLE Singers"])
        op.result()

    autocommit.enable_autocommit_mode(
        instance_id,
        sample_database.database_id,
    )
    out, _ = capsys.readouterr()
    assert "Autocommit mode is enabled." in out
    assert "SingerId: 13, AlbumId: Russell, AlbumTitle: Morales" in out
