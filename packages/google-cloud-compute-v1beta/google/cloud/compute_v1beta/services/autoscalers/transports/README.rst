
transport inheritance structure
_______________________________

``AutoscalersTransport`` is the ABC for all transports.

- public child ``AutoscalersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutoscalersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutoscalersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutoscalersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
