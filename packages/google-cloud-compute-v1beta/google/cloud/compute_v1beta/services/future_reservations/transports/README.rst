
transport inheritance structure
_______________________________

``FutureReservationsTransport`` is the ABC for all transports.

- public child ``FutureReservationsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``FutureReservationsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseFutureReservationsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``FutureReservationsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
