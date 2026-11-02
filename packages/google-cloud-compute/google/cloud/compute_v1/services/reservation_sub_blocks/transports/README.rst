
transport inheritance structure
_______________________________

``ReservationSubBlocksTransport`` is the ABC for all transports.

- public child ``ReservationSubBlocksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReservationSubBlocksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReservationSubBlocksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReservationSubBlocksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
