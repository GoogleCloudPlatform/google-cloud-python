
transport inheritance structure
_______________________________

``BrowserServiceTransport`` is the ABC for all transports.

- public child ``BrowserServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BrowserServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBrowserServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BrowserServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
