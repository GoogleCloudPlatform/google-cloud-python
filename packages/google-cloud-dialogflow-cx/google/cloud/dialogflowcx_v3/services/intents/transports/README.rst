
transport inheritance structure
_______________________________

``IntentsTransport`` is the ABC for all transports.

- public child ``IntentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``IntentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseIntentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``IntentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
