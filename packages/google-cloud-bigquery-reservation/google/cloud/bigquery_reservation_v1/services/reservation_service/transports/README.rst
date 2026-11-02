
transport inheritance structure
_______________________________

``ReservationServiceTransport`` is the ABC for all transports.

- public child ``ReservationServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ReservationServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseReservationServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ReservationServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
