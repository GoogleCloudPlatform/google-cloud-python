
transport inheritance structure
_______________________________

``AssistantServiceTransport`` is the ABC for all transports.

- public child ``AssistantServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AssistantServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAssistantServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AssistantServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
