
transport inheritance structure
_______________________________

``CrossNetworkAutomationServiceTransport`` is the ABC for all transports.

- public child ``CrossNetworkAutomationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CrossNetworkAutomationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCrossNetworkAutomationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CrossNetworkAutomationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
