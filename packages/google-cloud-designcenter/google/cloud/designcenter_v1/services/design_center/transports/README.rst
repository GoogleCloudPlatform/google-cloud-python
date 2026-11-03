
transport inheritance structure
_______________________________

``DesignCenterTransport`` is the ABC for all transports.

- public child ``DesignCenterGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DesignCenterGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDesignCenterRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DesignCenterRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
