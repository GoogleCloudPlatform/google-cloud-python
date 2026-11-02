
transport inheritance structure
_______________________________

``ReservationBlocksTransport`` is the ABC for all transports.

- public child ``ReservationBlocksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReservationBlocksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReservationBlocksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReservationBlocksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
