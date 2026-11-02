
transport inheritance structure
_______________________________

``ParameterManagerTransport`` is the ABC for all transports.

- public child ``ParameterManagerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ParameterManagerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseParameterManagerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ParameterManagerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
