import pytest

import google.auth
import grpc

# Define the parametrized data
vary_transport = [
    (
        grpc.insecure_channel,
        "grpc",
        "localhost:7469",
        "googleapis.com",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "rest",
        "localhost:7469",
        "googleapis.com",
        "googleapis.com",
    ),
]

vary_channel_transport_endpoints_universes = [
    (
        grpc.insecure_channel,
        "grpc",
        "showcase.googleapis.com",
        "showcase.googleapis.com",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "grpc",
        "showcase.googleapis.com",
        "localhost:7469",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "grpc",
        "localhost:7469",
        "showcase.googleapis.com",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "grpc",
        "localhost:7469",
        "localhost:7469",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "rest",
        "showcase.googleapis.com",
        "showcase.googleapis.com",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "rest",
        "showcase.googleapis.com",
        "localhost:7469",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "rest",
        "localhost:7469",
        "showcase.googleapis.com",
        "googleapis.com",
    ),
    (
        grpc.insecure_channel,
        "rest",
        "localhost:7469",
        "localhost:7469",
        "googleapis.com",
    ),
]


@pytest.mark.parametrize(
    "channel_creator, transport_name, transport_endpoint, credential_universe, client_universe",
    vary_transport,
)
def test_universe_domain_validation_pass(
    parametrized_echo,
    channel_creator,
    transport_name,
    transport_endpoint,
    credential_universe,
    client_universe,
):
    # Test that only the configured client universe and credentials universe are used for validation
    assert parametrized_echo.universe_domain == client_universe
    # TODO: This is needed to cater for older versions of google-auth
    # Make this test unconditional once the minimum supported version of
    # google-auth becomes 2.23.0 or higher.
    google_auth_major, google_auth_minor = [
        int(part) for part in google.auth.__version__.split(".")[0:2]
    ]
    if google_auth_major > 2 or (google_auth_major == 2 and google_auth_minor >= 23):
        assert (
            parametrized_echo.transport._credentials.universe_domain
            == credential_universe
        )
    if transport_name == "rest":
        assert parametrized_echo.api_endpoint == "http://" + transport_endpoint
    else:
        assert parametrized_echo.api_endpoint == transport_endpoint
    response = parametrized_echo.echo({"content": "Universe validation succeeded!"})
    assert response.content == "Universe validation succeeded!"


# TODO: Test without passing a channel to gRPC transports in the test fixture
# TODO: Test without creating a transport in the test fixture
# TODO: Test asynchronous client as well.
# @pytest.mark.parametrize("channel_creator", [grpc.insecure_channel, None])


@pytest.mark.parametrize(
    "channel_creator, transport_name, transport_endpoint, credential_universe, client_universe",
    vary_channel_transport_endpoints_universes,
)
def test_universe_domain_validation_fail(
    parametrized_echo,
    channel_creator,
    transport_name,
    transport_endpoint,
    credential_universe,
    client_universe,
):
    """Test that only the client and credentials universes are used for validation, and not the endpoint."""
    assert parametrized_echo.universe_domain == client_universe
    # TODO: This is needed to cater for older versions of google-auth
    # Make this test unconditional once the minimum supported version of
    # google-auth becomes 2.23.0 or higher.
    google_auth_major, google_auth_minor, _ = [
        part for part in google.auth.__version__.split(".")
    ]
    if int(google_auth_major) > 2 or (
        int(google_auth_major) == 2 and int(google_auth_minor) >= 23
    ):
        assert (
            parametrized_echo.transport._credentials.universe_domain
            == credential_universe
        )
        if transport_name == "rest":
            assert parametrized_echo.api_endpoint == "http://" + transport_endpoint
        elif channel_creator == grpc.insecure_channel:
            # TODO: Investigate where this endpoint override is coming from
            assert parametrized_echo.api_endpoint == "localhost:7469"
        else:
            assert parametrized_echo.api_endpoint == transport_endpoint

        # NOTE (b/349488459): universe validation is disabled until further notice.
        # with pytest.raises(ValueError) as err:
        #     parametrized_echo.echo({
        #         'content': 'Universe validation failed!'
        #         })
        # assert str(
        #     err.value) == f"The configured universe domain ({client_universe}) does not match the universe domain found in the credentials ({credential_universe}). If you haven't configured the universe domain explicitly, `googleapis.com` is the default."
