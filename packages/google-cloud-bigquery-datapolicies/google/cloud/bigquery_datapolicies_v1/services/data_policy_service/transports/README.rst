
transport inheritance structure
_______________________________

``DataPolicyServiceTransport`` is the ABC for all transports.

- public child ``DataPolicyServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataPolicyServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataPolicyServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataPolicyServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
