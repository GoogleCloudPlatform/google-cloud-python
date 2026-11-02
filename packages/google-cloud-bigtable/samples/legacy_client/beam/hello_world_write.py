# Copyright 2020 Google Inc.
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
import datetime

import apache_beam as beam
from apache_beam.io.gcp.bigtableio import WriteToBigTable
from apache_beam.options.pipeline_options import PipelineOptions

from google.cloud.bigtable import row


class BigtableOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            "--bigtable-project",
            help="The Bigtable project ID, this can be different than your "
            "Dataflow project",
            default="bigtable-project",
        )
        parser.add_argument(
            "--bigtable-instance",
            help="The Bigtable instance ID",
            default="bigtable-instance",
        )
        parser.add_argument(
            "--bigtable-table",
            help="The Bigtable table ID in the instance.",
            default="bigtable-table",
        )


class CreateRowFn(beam.DoFn):
    def process(self, key):
        direct_row = row.DirectRow(row_key=key)
        direct_row.set_cell(
            "stats_summary", b"os_build", b"android", datetime.datetime.now()
        )
        return [direct_row]


def run(argv=None):
    """Build and run the pipeline."""
    options = BigtableOptions(argv)
    with beam.Pipeline(options=options) as p:
        (
            p
            | beam.Create(["phone#4c410523#20190501", "phone#4c410523#20190502"])
            | beam.ParDo(CreateRowFn())
            | WriteToBigTable(
                project_id=options.bigtable_project,
                instance_id=options.bigtable_instance,
                table_id=options.bigtable_table,
            )
        )


if __name__ == "__main__":
    run()
