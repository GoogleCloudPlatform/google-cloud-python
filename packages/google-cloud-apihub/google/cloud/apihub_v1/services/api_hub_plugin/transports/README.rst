
transport inheritance structure
_______________________________

``ApiHubPluginTransport`` is the ABC for all transports.

- public child ``ApiHubPluginGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ApiHubPluginGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseApiHubPluginRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ApiHubPluginRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
