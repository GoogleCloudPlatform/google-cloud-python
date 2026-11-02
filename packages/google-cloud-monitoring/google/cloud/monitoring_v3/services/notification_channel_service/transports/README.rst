
transport inheritance structure
_______________________________

``NotificationChannelServiceTransport`` is the ABC for all transports.

- public child ``NotificationChannelServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NotificationChannelServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNotificationChannelServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NotificationChannelServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
