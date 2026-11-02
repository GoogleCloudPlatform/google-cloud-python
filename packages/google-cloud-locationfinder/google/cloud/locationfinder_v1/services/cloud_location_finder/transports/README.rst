
transport inheritance structure
_______________________________

``CloudLocationFinderTransport`` is the ABC for all transports.

- public child ``CloudLocationFinderGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudLocationFinderGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudLocationFinderRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudLocationFinderRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
