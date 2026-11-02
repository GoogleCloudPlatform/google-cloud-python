
transport inheritance structure
_______________________________

``WorkstationsTransport`` is the ABC for all transports.

- public child ``WorkstationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``WorkstationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseWorkstationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``WorkstationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
