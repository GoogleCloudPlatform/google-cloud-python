# -*- coding: utf-8 -*-
# this was previously implemented using the `snapshottest` package (https://goo.gl/zC4yUc),
# which is not compatible with Python 3.12. So we moved to a standard dictionary storing
# expected outputs for each test
from __future__ import unicode_literals

snapshots = {}

snapshots["test_read_row_partial"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_rows"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_row_range"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_row_ranges"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_prefix"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_filter"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family stats_summary
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family stats_summary
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots["test_read_row"] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

"""
