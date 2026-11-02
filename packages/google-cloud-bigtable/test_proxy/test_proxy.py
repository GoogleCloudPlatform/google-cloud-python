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
The Python implementation of the `cloud-bigtable-clients-test` proxy server.

https://github.com/googleapis/cloud-bigtable-clients-test

This server is intended to be used to test the correctness of Bigtable
clients across languages.

Contributor Note: the proxy implementation is split across TestProxyClientHandler
and TestProxyGrpcServer. This is due to the fact that generated protos and proto-plus
objects cannot be used in the same process, so we had to make use of the
multiprocessing module to allow them to work together.
"""

import multiprocessing
import argparse
import sys
import os
sys.path.append("handlers")


def grpc_server_process(request_q, queue_pool, port=50055):
    """
    Defines a process that hosts a grpc server
    proxies requests to a client_handler_process
    """
    sys.path.append("protos")
    from concurrent import futures

    import grpc
    import test_proxy_pb2_grpc
    import grpc_handler

    # Start gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_proxy_pb2_grpc.add_CloudBigtableV2TestProxyServicer_to_server(
        grpc_handler.TestProxyGrpcServer(request_q, queue_pool), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("grpc_server_process started, listening on " + port)
    server.wait_for_termination()


async def client_handler_process_async(request_q, queue_pool, client_type="async"):
    """
    Defines a process that recives Bigtable requests from a grpc_server_process,
    and runs the request using a client library instance
    """
    import base64
    import re
    import asyncio
    import warnings
    import client_handler_data_async
    warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*Bigtable emulator.*")

    def camel_to_snake(str):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", str).lower()

    def format_dict(input_obj):
        if isinstance(input_obj, list):
            return [format_dict(x) for x in input_obj]
        elif isinstance(input_obj, dict):
            return {camel_to_snake(k): format_dict(v) for k, v in input_obj.items()}
        elif isinstance(input_obj, str):
            # check for time encodings
            if re.match("^[0-9]+s$", input_obj):
                return int(input_obj[:-1])
            # check for encoded bytes
            if re.match("^[A-Za-z0-9+/=]+$", input_obj):
                try:
                    decoded_str = base64.b64decode(input_obj)
                    # if the string contains non-ascii bytes, raise exception
                    decoded_str.decode("ascii")
                    return decoded_str
                except Exception:
                    pass
            # check for int strings
            try:
                return int(input_obj)
            except (ValueError, TypeError):
                return input_obj
        else:
            return input_obj

    # Listen to requests from grpc server process
    print_msg = f"client_handler_process started with client_type={client_type}"
    print(print_msg)
    client_map = {}
    background_tasks = set()
    while True:
        if not request_q.empty():
            json_data = format_dict(request_q.get())
            fn_name = json_data.pop("proxy_request")
            print(f"--- running {fn_name} with {json_data}")
            out_q = queue_pool[json_data.pop("response_queue_idx")]
            client_id = json_data.pop("client_id")
            client = client_map.get(client_id, None)
            # handle special cases for client creation and deletion
            if fn_name == "CreateClient":
                if client_type == "legacy":
                    import client_handler_legacy
                    client = client_handler_legacy.LegacyTestProxyClientHandler(**json_data)
                elif client_type == "sync":
                    import client_handler_data_sync_autogen
                    client = client_handler_data_sync_autogen.TestProxyClientHandler(**json_data)
                else:
                    client = client_handler_data_async.TestProxyClientHandlerAsync(**json_data)
                client_map[client_id] = client
                out_q.put(True)
            elif client is None:
                out_q.put(RuntimeError("client not found"))
            elif fn_name == "CloseClient":
                client.close()
                out_q.put(True)
            elif fn_name == "RemoveClient":
                client_map.pop(client_id, None)
                out_q.put(True)
                print("")
            else:
                # run actual rpc against client
                async def _run_fn(out_q, fn, **kwargs):
                    result = await fn(**kwargs)
                    out_q.put(result)
                fn = getattr(client, fn_name)
                task = asyncio.create_task(_run_fn(out_q, fn, **json_data))
                await asyncio.sleep(0)
                background_tasks.add(task)
                task.add_done_callback(background_tasks.remove)
        await asyncio.sleep(0.01)


def client_handler_process(request_q, queue_pool, client_type="async"):
    """
    Sync entrypoint for client_handler_process_async
    """
    import asyncio
    asyncio.run(client_handler_process_async(request_q, queue_pool, client_type))


p = argparse.ArgumentParser()
p.add_argument("--port", dest='port', default="50055")
p.add_argument("--client_type", dest='client_type', default="async", choices=["async", "sync", "legacy"])

if __name__ == "__main__":
    port = p.parse_args().port
    client_type = p.parse_args().client_type

    # start and run both processes
    # larger pools support more concurrent requests
    response_queue_pool = [multiprocessing.Queue() for _ in range(100)]
    request_q = multiprocessing.Queue()

    CLIENT_IS_FOREGROUND=bool(os.environ.get("CLIENT_IS_FOREGROUND", True))
    if CLIENT_IS_FOREGROUND:
        # run client in forground and proxy in background
        # breakpoints can be attached to handlers/client_handler_data.py
        proxy = multiprocessing.Process(
            target=grpc_server_process,
            args=(
                request_q,
                response_queue_pool,
                port
            ),
        )
        proxy.start()
        client_handler_process(request_q, response_queue_pool, client_type)
        proxy.join()
    else:
        # run proxy in forground and client in background
        # breakpoints can be attached to handlers/grpc_handler.py
        client = multiprocessing.Process(
            target=client_handler_process,
            args=(
                request_q,
                response_queue_pool,
            ),
        )
        client.start()
        grpc_server_process(request_q, response_queue_pool, port)
        client.join()
