def test_index_route(test_client):
    """test_index_route
    GIVEN a client app interface
    WHEN a request is made
    THEN check the page status code, and some core elements
    """

    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Hello, world!" in response.data
    assert b"Sign In" in response.data
    assert b"Sign Up" in response.data


def test_signin_route(test_client):
    """test_signin_route
    GIVEN a client app interface
    WHEN a request is made
    THEN check the page status code, and some core elements
    """

    response = test_client.get("/sign-in")

    assert response.status_code == 200
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Remember me" in response.data
    assert b"Sign in" in response.data


def test_signup_route(test_client):
    """test_signup_route
    GIVEN a client app interface
    WHEN a request is made
    THEN check the page status code, and some core elements
    """

    response = test_client.get("/sign-up")

    assert response.status_code == 200
    assert b"User" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data
    assert b"Password confirmation" in response.data
    assert b"Role" in response.data
    assert b"Sign up" in response.data
    assert b"Back" in response.data
