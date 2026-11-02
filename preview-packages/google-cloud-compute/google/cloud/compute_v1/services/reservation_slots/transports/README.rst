
transport inheritance structure
_______________________________

``ReservationSlotsTransport`` is the ABC for all transports.

- public child ``ReservationSlotsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReservationSlotsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReservationSlotsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReservationSlotsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
