
transport inheritance structure
_______________________________

``TelcoAutomationTransport`` is the ABC for all transports.

- public child ``TelcoAutomationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TelcoAutomationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTelcoAutomationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TelcoAutomationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
