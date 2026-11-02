
transport inheritance structure
_______________________________

``ConfigServiceV2Transport`` is the ABC for all transports.

- public child ``ConfigServiceV2GrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ConfigServiceV2GrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseConfigServiceV2RestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ConfigServiceV2RestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
