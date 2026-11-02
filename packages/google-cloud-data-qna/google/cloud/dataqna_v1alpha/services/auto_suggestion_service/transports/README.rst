
transport inheritance structure
_______________________________

``AutoSuggestionServiceTransport`` is the ABC for all transports.

- public child ``AutoSuggestionServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AutoSuggestionServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAutoSuggestionServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AutoSuggestionServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
