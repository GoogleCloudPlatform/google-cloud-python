
transport inheritance structure
_______________________________

``FulfillmentsTransport`` is the ABC for all transports.

- public child ``FulfillmentsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FulfillmentsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFulfillmentsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FulfillmentsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
