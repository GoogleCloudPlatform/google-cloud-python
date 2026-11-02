
transport inheritance structure
_______________________________

``ValidationHelperV1Transport`` is the ABC for all transports.

- public child ``ValidationHelperV1GrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ValidationHelperV1GrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseValidationHelperV1RestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ValidationHelperV1RestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
