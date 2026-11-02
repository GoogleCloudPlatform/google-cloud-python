
transport inheritance structure
_______________________________

``DataLabelingServiceTransport`` is the ABC for all transports.

- public child ``DataLabelingServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DataLabelingServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDataLabelingServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DataLabelingServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
