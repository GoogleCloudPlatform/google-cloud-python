
transport inheritance structure
_______________________________

``InterceptTransport`` is the ABC for all transports.

- public child ``InterceptGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InterceptGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInterceptRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InterceptRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
