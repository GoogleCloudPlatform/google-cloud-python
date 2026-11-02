import time
import traceback

import requests


def start_grpc_server(grpc_endpoint, http_endpoint):
    """Starts the testbench gRPC server if it's not already running.

    this essentially makes -

    `curl -s --retry 5 --retry-max-time 40 "http://localhost:9000/start_grpc?port=8888"`
    """
    start_time = time.time()
    max_time = 40
    retries = 5
    port = grpc_endpoint.split(":")[-1]
    url = f"{http_endpoint}/start_grpc?port={port}"

    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return
        except requests.exceptions.RequestException:
            print("Failed to create grpc server", traceback.format_exc())
            raise

        elapsed_time = time.time() - start_time
        if elapsed_time >= max_time:
            raise RuntimeError("Failed to start gRPC server within the time limit.")

        # backoff
        time.sleep(1)
