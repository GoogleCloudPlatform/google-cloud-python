
transport inheritance structure
_______________________________

``WorkloadManagerTransport`` is the ABC for all transports.

- public child ``WorkloadManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkloadManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkloadManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkloadManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
