
transport inheritance structure
_______________________________

``RolloutPlansTransport`` is the ABC for all transports.

- public child ``RolloutPlansGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RolloutPlansGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRolloutPlansRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RolloutPlansRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
