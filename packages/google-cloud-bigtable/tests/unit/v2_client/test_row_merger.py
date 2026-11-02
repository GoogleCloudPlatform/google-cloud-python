import os

import proto

from google.cloud.bigtable.row_data import PartialRowData
from google.cloud.bigtable_v2.types.bigtable import ReadRowsResponse


# TODO: autogenerate protos from
#  https://github.com/googleapis/conformance-tests/blob/main/bigtable/v2/proto/google/cloud/conformance/bigtable/v2/tests.proto
class ReadRowsTest(proto.Message):
    class Result(proto.Message):
        row_key = proto.Field(proto.STRING, number=1)
        family_name = proto.Field(proto.STRING, number=2)
        qualifier = proto.Field(proto.STRING, number=3)
        timestamp_micros = proto.Field(proto.INT64, number=4)
        value = proto.Field(proto.STRING, number=5)
        label = proto.Field(proto.STRING, number=6)
        error = proto.Field(proto.BOOL, number=7)

    description = proto.Field(proto.STRING, number=1)
    chunks = proto.RepeatedField(
        proto.MESSAGE, number=2, message=ReadRowsResponse.CellChunk
    )
    results = proto.RepeatedField(proto.MESSAGE, number=3, message=Result)


class TestFile(proto.Message):
    __test__ = False
    read_rows_tests = proto.RepeatedField(proto.MESSAGE, number=1, message=ReadRowsTest)


def parse_readrows_acceptance_tests():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "read-rows-acceptance-test.json")

    with open(filename) as json_file:
        test_json = TestFile.from_json(json_file.read())
        return test_json.read_rows_tests


def extract_results_from_row(row: PartialRowData):
    results = []
    for family, col_dict in row.cells.items():
        for col, cells in col_dict.items():
            for cell in cells:
                results.append(
                    ReadRowsTest.Result(
                        row_key=row.row_key,
                        family_name=family,
                        qualifier=col,
                        timestamp_micros=cell.timestamp_micros,
                        value=cell.value,
                        label=(cell.labels[0] if cell.labels else ""),
                    )
                )
    return results
