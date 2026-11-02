
transport inheritance structure
_______________________________

``TransitionRouteGroupsTransport`` is the ABC for all transports.

- public child ``TransitionRouteGroupsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TransitionRouteGroupsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTransitionRouteGroupsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TransitionRouteGroupsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
