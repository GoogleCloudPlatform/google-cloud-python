
transport inheritance structure
_______________________________

``WorkerPoolsTransport`` is the ABC for all transports.

- public child ``WorkerPoolsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkerPoolsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkerPoolsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkerPoolsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
