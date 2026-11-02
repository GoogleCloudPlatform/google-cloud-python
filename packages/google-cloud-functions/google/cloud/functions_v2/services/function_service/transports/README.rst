
transport inheritance structure
_______________________________

``FunctionServiceTransport`` is the ABC for all transports.

- public child ``FunctionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FunctionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFunctionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FunctionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
