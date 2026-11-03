# -*- coding: utf-8 -*-
# this was previously implemented using the `snapshottest` package (https://goo.gl/zC4yUc),
# which is not compatible with Python 3.12. So we moved to a standard dictionary storing
# expected outputs for each test
from __future__ import unicode_literals

snapshots = {}

snapshots["test_filter_limit_row_regex"] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_cells_per_col"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_cells_per_row"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_cells_per_row_offset"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family stats_summary
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family stats_summary
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_col_family_regex"
] = """Reading data for phone#4c410523#20190501:
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

snapshots[
    "test_filter_limit_col_qualifier_regex"
] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00

"""

snapshots["test_filter_limit_col_range"] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_value_range"
] = """Reading data for phone#4c410523#20190501:
Column Family stats_summary
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family stats_summary
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_limit_value_regex"
] = """Reading data for phone#4c410523#20190501:
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

snapshots[
    "test_filter_limit_timestamp_range"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00

"""

snapshots["test_filter_limit_block_all"] = ""

snapshots["test_filter_limit_pass_all"] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_modify_strip_value"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb:  @2019-05-01 00:00:00+00:00
\tdata_plan_01gb:  @2019-04-30 23:00:00+00:00
\tdata_plan_05gb:  @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell:  @2019-05-01 00:00:00+00:00
\tconnected_wifi:  @2019-05-01 00:00:00+00:00
\tos_build:  @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb:  @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell:  @2019-05-01 00:00:00+00:00
\tconnected_wifi:  @2019-05-01 00:00:00+00:00
\tos_build:  @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb:  @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell:  @2019-05-01 00:00:00+00:00
\tconnected_wifi:  @2019-05-01 00:00:00+00:00
\tos_build:  @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb:  @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell:  @2019-05-01 00:00:00+00:00
\tconnected_wifi:  @2019-05-01 00:00:00+00:00
\tos_build:  @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb:  @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tconnected_cell:  @2019-05-01 00:00:00+00:00
\tconnected_wifi:  @2019-05-01 00:00:00+00:00
\tos_build:  @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_modify_apply_label"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00 [labelled]
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00 [labelled]
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [labelled]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00 [labelled]

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [labelled]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00 [labelled]

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [labelled]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00 [labelled]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00 [labelled]

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00 [labelled]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00 [labelled]

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00 [labelled]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [labelled]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00 [labelled]
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00 [labelled]

"""

snapshots["test_filter_composing_chain"] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_composing_interleave"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00
Column Family stats_summary
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00

"""

snapshots[
    "test_filter_composing_condition"
] = """Reading data for phone#4c410523#20190501:
Column Family cell_plan
\tdata_plan_01gb: false @2019-05-01 00:00:00+00:00 [filtered-out]
\tdata_plan_01gb: true @2019-04-30 23:00:00+00:00 [filtered-out]
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [filtered-out]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [filtered-out]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [filtered-out]
\tos_build: PQ2A.190405.003 @2019-05-01 00:00:00+00:00 [filtered-out]

Reading data for phone#4c410523#20190502:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [filtered-out]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [filtered-out]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [filtered-out]
\tos_build: PQ2A.190405.004 @2019-05-01 00:00:00+00:00 [filtered-out]

Reading data for phone#4c410523#20190505:
Column Family cell_plan
\tdata_plan_05gb: true @2019-05-01 00:00:00+00:00 [filtered-out]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00 [filtered-out]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [filtered-out]
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00 [filtered-out]

Reading data for phone#5c10102#20190501:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00 [passed-filter]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [passed-filter]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [passed-filter]
\tos_build: PQ2A.190401.002 @2019-05-01 00:00:00+00:00 [passed-filter]

Reading data for phone#5c10102#20190502:
Column Family cell_plan
\tdata_plan_10gb: true @2019-05-01 00:00:00+00:00 [passed-filter]
Column Family stats_summary
\tconnected_cell: \x00\x00\x00\x00\x00\x00\x00\x01 @2019-05-01 00:00:00+00:00 [passed-filter]
\tconnected_wifi: \x00\x00\x00\x00\x00\x00\x00\x00 @2019-05-01 00:00:00+00:00 [passed-filter]
\tos_build: PQ2A.190406.000 @2019-05-01 00:00:00+00:00 [passed-filter]

"""
