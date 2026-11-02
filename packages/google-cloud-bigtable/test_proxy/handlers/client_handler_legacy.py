# Copyright 2023 Google LLC
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
"""
This module contains the client handler process for proxy_server.py.
"""
import os

from google.cloud.environment_vars import BIGTABLE_EMULATOR
from google.cloud.bigtable.client import Client

import client_handler_data_async as client_handler

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class LegacyTestProxyClientHandler(client_handler.TestProxyClientHandlerAsync):

    def __init__(
        self,
        data_target=None,
        project_id=None,
        instance_id=None,
        app_profile_id=None,
        per_operation_timeout=None,
        **kwargs,
    ):
        self.closed = False
        # use emulator
        os.environ[BIGTABLE_EMULATOR] = data_target
        self.client = Client(project=project_id)
        self.instance_id = instance_id
        self.app_profile_id = app_profile_id
        self.per_operation_timeout = per_operation_timeout

    def close(self):
        self.closed = True

    @client_handler.error_safe
    async def ReadRows(self, request, **kwargs):
        table_id = request["table_name"].split("/")[-1]
        # app_profile_id = self.app_profile_id or request.get("app_profile_id", None)
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)

        limit = request.get("rows_limit", None)
        start_key = request.get("rows", {}).get("row_keys", [None])[0]
        end_key = request.get("rows", {}).get("row_keys", [None])[-1]
        end_inclusive = request.get("rows", {}).get("row_ranges", [{}])[-1].get("end_key_closed", True)

        row_list = []
        for row in table.read_rows(start_key=start_key, end_key=end_key, limit=limit, end_inclusive=end_inclusive):
            # parse results into proto formatted dict
            dict_val = {"row_key": row.row_key}
            for family, family_cells in row.cells.items():
                family_dict = {"name": family}
                for qualifier, qualifier_cells in family_cells.items():
                    column_dict = {"qualifier": qualifier}
                    for cell in qualifier_cells:
                        cell_dict = {
                            "value": cell.value,
                            "timestamp_micros": cell.timestamp.timestamp() * 1000000,
                            "labels": cell.labels,
                        }
                        column_dict.setdefault("cells", []).append(cell_dict)
                    family_dict.setdefault("columns", []).append(column_dict)
                dict_val.setdefault("families", []).append(family_dict)
            row_list.append(dict_val)
        return row_list

    @client_handler.error_safe
    async def ReadRow(self, row_key, **kwargs):
        table_id = kwargs["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)

        row = table.read_row(row_key)
        # parse results into proto formatted dict
        dict_val = {"row_key": row.row_key}
        for family, family_cells in row.cells.items():
            family_dict = {"name": family}
            for qualifier, qualifier_cells in family_cells.items():
                column_dict = {"qualifier": qualifier}
                for cell in qualifier_cells:
                    cell_dict = {
                        "value": cell.value,
                        "timestamp_micros": cell.timestamp.timestamp() * 1000000,
                        "labels": cell.labels,
                    }
                    column_dict.setdefault("cells", []).append(cell_dict)
                family_dict.setdefault("columns", []).append(column_dict)
            dict_val.setdefault("families", []).append(family_dict)
        return dict_val

    @client_handler.error_safe
    async def MutateRow(self, request, **kwargs):
        from datetime import datetime
        from google.cloud.bigtable.row import DirectRow
        table_id = request["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)
        row_key = request["row_key"]
        new_row = DirectRow(row_key, table)
        for m_dict in request.get("mutations", []):
            details = m_dict.get("set_cell") or m_dict.get("delete_from_column") or m_dict.get("delete_from_family") or m_dict.get("delete_from_row")
            timestamp = datetime.fromtimestamp(details.get("timestamp_micros")) if details.get("timestamp_micros") else None
            if m_dict.get("set_cell"):
                new_row.set_cell(details["family_name"], details["column_qualifier"], details["value"], timestamp=timestamp)
            elif m_dict.get("delete_from_column"):
                new_row.delete_cell(details["family_name"], details["column_qualifier"], timestamp=timestamp)
            elif m_dict.get("delete_from_family"):
                new_row.delete_cells(details["family_name"], timestamp=timestamp)
            elif m_dict.get("delete_from_row"):
                new_row.delete()
        table.mutate_rows([new_row])
        return "OK"

    @client_handler.error_safe
    async def BulkMutateRows(self, request, **kwargs):
        from google.cloud.bigtable.row import DirectRow
        from datetime import datetime
        table_id = request["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)
        rows = []
        for entry in request.get("entries", []):
            row_key = entry["row_key"]
            new_row = DirectRow(row_key, table)
            for m_dict in entry.get("mutations"):
                details = m_dict.get("set_cell") or m_dict.get("delete_from_column") or m_dict.get("delete_from_family") or m_dict.get("delete_from_row")
                timestamp = datetime.fromtimestamp(details.get("timestamp_micros")) if details.get("timestamp_micros") else None
                if m_dict.get("set_cell"):
                    new_row.set_cell(details["family_name"], details["column_qualifier"], details["value"], timestamp=timestamp)
                elif m_dict.get("delete_from_column"):
                    new_row.delete_cell(details["family_name"], details["column_qualifier"], timestamp=timestamp)
                elif m_dict.get("delete_from_family"):
                    new_row.delete_cells(details["family_name"], timestamp=timestamp)
                elif m_dict.get("delete_from_row"):
                    new_row.delete()
            rows.append(new_row)
        table.mutate_rows(rows)
        return "OK"

    @client_handler.error_safe
    async def CheckAndMutateRow(self, request, **kwargs):
        from google.cloud.bigtable.row import ConditionalRow
        from google.cloud.bigtable.row_filters import PassAllFilter
        table_id = request["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)

        predicate_filter = request.get("predicate_filter", PassAllFilter(True))
        new_row = ConditionalRow(request["row_key"], table, predicate_filter)

        combined_mutations = [{"state": True, **m} for m in request.get("true_mutations", [])]
        combined_mutations.extend([{"state": False, **m} for m in request.get("false_mutations", [])])
        for mut_dict in combined_mutations:
            if "set_cell" in mut_dict:
                details = mut_dict["set_cell"]
                new_row.set_cell(
                    details.get("family_name", ""),
                    details.get("column_qualifier", ""),
                    details.get("value", ""),
                    timestamp=details.get("timestamp_micros", None),
                    state=mut_dict["state"],
                )
            elif "delete_from_column" in mut_dict:
                details = mut_dict["delete_from_column"]
                new_row.delete_cell(
                    details.get("family_name", ""),
                    details.get("column_qualifier", ""),
                    timestamp=details.get("timestamp_micros", None),
                    state=mut_dict["state"],
                )
            elif "delete_from_family" in mut_dict:
                details = mut_dict["delete_from_family"]
                new_row.delete_cells(
                    details.get("family_name", ""),
                    timestamp=details.get("timestamp_micros", None),
                    state=mut_dict["state"],
                )
            elif "delete_from_row" in mut_dict:
                new_row.delete(state=mut_dict["state"])
            else:
                raise RuntimeError(f"Unknown mutation type: {mut_dict}")
            return new_row.commit()

    @client_handler.error_safe
    async def ReadModifyWriteRow(self, request, **kwargs):
        from google.cloud.bigtable.row import AppendRow
        from google.cloud._helpers import _microseconds_from_datetime
        table_id = request["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)
        row_key = request["row_key"]
        new_row = AppendRow(row_key, table)
        for rule_dict in request.get("rules", []):
            qualifier = rule_dict["column_qualifier"]
            family = rule_dict["family_name"]
            if "append_value" in rule_dict:
                new_row.append_cell_value(family, qualifier, rule_dict["append_value"])
            else:
                new_row.increment_cell_value(family, qualifier, rule_dict["increment_amount"])
        raw_result = new_row.commit()
        result_families = []
        for family, column_dict in raw_result.items():
            result_columns = []
            for column, cell_list in column_dict.items():
                result_cells = []
                for cell_tuple in cell_list:
                    cell_dict = {"value": cell_tuple[0], "timestamp_micros": _microseconds_from_datetime(cell_tuple[1])}
                    result_cells.append(cell_dict)
                result_columns.append({"qualifier": column, "cells": result_cells})
            result_families.append({"name": family, "columns": result_columns})
        return {"key": row_key, "families": result_families}

    @client_handler.error_safe
    async def SampleRowKeys(self, request, **kwargs):
        table_id = request["table_name"].split("/")[-1]
        instance = self.client.instance(self.instance_id)
        table = instance.table(table_id)
        response = list(table.sample_row_keys())
        tuple_response = [(s.row_key, s.offset_bytes) for s in response]
        return tuple_response
