
transport inheritance structure
_______________________________

``ProductInputsServiceTransport`` is the ABC for all transports.

- public child ``ProductInputsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProductInputsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProductInputsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProductInputsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
