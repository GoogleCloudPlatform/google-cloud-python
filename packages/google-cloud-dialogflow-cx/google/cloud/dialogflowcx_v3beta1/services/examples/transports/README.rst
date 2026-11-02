
transport inheritance structure
_______________________________

``ExamplesTransport`` is the ABC for all transports.

- public child ``ExamplesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ExamplesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseExamplesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ExamplesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
