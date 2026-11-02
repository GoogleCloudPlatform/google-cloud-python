
transport inheritance structure
_______________________________

``BinauthzManagementServiceV1Transport`` is the ABC for all transports.

- public child ``BinauthzManagementServiceV1GrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BinauthzManagementServiceV1GrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBinauthzManagementServiceV1RestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BinauthzManagementServiceV1RestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
