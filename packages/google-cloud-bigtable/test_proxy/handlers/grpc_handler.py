import time

import test_proxy_pb2
import test_proxy_pb2_grpc
import data_pb2
import bigtable_pb2
from google.rpc.status_pb2 import Status
from google.protobuf import json_format


def correct_cancelled(status):
    """
    Deadline exceeded errors are a race between client side cancellation and server
    side deadline exceeded. For the purpose of these tests, the client will never cancel,
    so we adjust cancelled errors to deadline_exceeded for consistency.
    """
    if status.code == 1:
        return Status(code=4, message="deadlineexceeded")
    return status


class TestProxyGrpcServer(test_proxy_pb2_grpc.CloudBigtableV2TestProxyServicer):
    """
    Implements a grpc server that proxies conformance test requests to the client library

    Due to issues with using protoc-compiled protos and client-library
    proto-plus objects in the same process, this server defers requests to
    matching methods in a TestProxyClientHandler instance in a separate
    process.
    This happens invisbly in the decorator @delegate_to_client_handler, with the
    results attached to each request as a client_response kwarg
    """

    def __init__(self, request_q, queue_pool):
        self.open_queues = list(range(len(queue_pool)))
        self.queue_pool = queue_pool
        self.request_q = request_q

    def delegate_to_client_handler(func, timeout_seconds=300):
        """
        Decorator that transparently passes a request to the client
        handler process, and then attaches the resonse to the wrapped call
        """

        def wrapper(self, request, context, **kwargs):
            deadline = time.time() + timeout_seconds
            json_dict = json_format.MessageToDict(request)
            out_idx = self.open_queues.pop()
            json_dict["proxy_request"] = func.__name__
            json_dict["response_queue_idx"] = out_idx
            out_q = self.queue_pool[out_idx]
            self.request_q.put(json_dict)
            # wait for response
            while time.time() < deadline:
                if not out_q.empty():
                    response = out_q.get()
                    self.open_queues.append(out_idx)
                    if isinstance(response, Exception):
                        raise response
                    else:
                        return func(
                            self,
                            request,
                            context,
                            client_response=response,
                            **kwargs,
                        )
                time.sleep(1e-4)

        return wrapper

    @delegate_to_client_handler
    def CreateClient(self, request, context, client_response=None):
        return test_proxy_pb2.CreateClientResponse()

    @delegate_to_client_handler
    def CloseClient(self, request, context, client_response=None):
        return test_proxy_pb2.CloseClientResponse()

    @delegate_to_client_handler
    def RemoveClient(self, request, context, client_response=None):
        return test_proxy_pb2.RemoveClientResponse()

    @delegate_to_client_handler
    def ReadRows(self, request, context, client_response=None):
        status = Status()
        rows = []
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(Status(code=5, message=client_response["error"]))
        else:
            rows = [data_pb2.Row(**d) for d in client_response]
        result = test_proxy_pb2.RowsResult(rows=rows, status=status)
        return result

    @delegate_to_client_handler
    def ReadRow(self, request, context, client_response=None):
        status = Status()
        row = None
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response.get("error"),
                )
            )
        elif client_response != "None":
            row = data_pb2.Row(**client_response)
        result = test_proxy_pb2.RowResult(row=row, status=status)
        return result

    @delegate_to_client_handler
    def MutateRow(self, request, context, client_response=None):
        status = Status()
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response["error"],
                )
            )
        return test_proxy_pb2.MutateRowResult(status=status)

    @delegate_to_client_handler
    def BulkMutateRows(self, request, context, client_response=None):
        status = Status()
        entries = []
        if isinstance(client_response, dict) and "error" in client_response:
            entries = [
                bigtable_pb2.MutateRowsResponse.Entry(
                    index=exc_dict.get("index", 1),
                    status=correct_cancelled(Status(code=exc_dict.get("code", 5))),
                )
                for exc_dict in client_response.get("subexceptions", [])
            ]
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response["error"],
                )
            )
        response = test_proxy_pb2.MutateRowsResult(status=status, entries=entries)
        return response

    @delegate_to_client_handler
    def CheckAndMutateRow(self, request, context, client_response=None):
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response["error"],
                )
            )
            response = test_proxy_pb2.CheckAndMutateRowResult(status=status)
        else:
            result = bigtable_pb2.CheckAndMutateRowResponse(
                predicate_matched=client_response
            )
            response = test_proxy_pb2.CheckAndMutateRowResult(
                result=result, status=Status()
            )
        return response

    @delegate_to_client_handler
    def ReadModifyWriteRow(self, request, context, client_response=None):
        status = Status()
        row = None
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response.get("error"),
                )
            )
        elif client_response != "None":
            row = data_pb2.Row(**client_response)
        result = test_proxy_pb2.RowResult(row=row, status=status)
        return result

    @delegate_to_client_handler
    def SampleRowKeys(self, request, context, client_response=None):
        status = Status()
        sample_list = []
        if isinstance(client_response, dict) and "error" in client_response:
            status = correct_cancelled(
                Status(
                    code=client_response.get("code", 5),
                    message=client_response.get("error"),
                )
            )
        else:
            for sample in client_response:
                sample_list.append(
                    bigtable_pb2.SampleRowKeysResponse(
                        offset_bytes=sample[1], row_key=sample[0]
                    )
                )
        return test_proxy_pb2.SampleRowKeysResult(status=status, samples=sample_list)

    @delegate_to_client_handler
    def ExecuteQuery(self, request, context, client_response=None):
        if isinstance(client_response, dict) and "error" in client_response:
            return test_proxy_pb2.ExecuteQueryResult(
                status=correct_cancelled(
                    Status(code=client_response.get("code", 13), message=client_response["error"])
                )
            )
        else:
            return test_proxy_pb2.ExecuteQueryResult(
                metadata=client_response["metadata"], rows=client_response["rows"]
            )
