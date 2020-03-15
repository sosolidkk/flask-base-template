import pytest
from app.models import User
from app import app


@pytest.fixture
def user():
    """Return a temporary user model
    """

    user = User(username="test_user", email="test@gmail.com", role=0)
    user.set_password("test_password")
    return user


@pytest.fixture
def test_client():
    """Return a flask app instance
    """

    testing_client = app.test_client()
    context = app.app_context()
    context.push()

    yield testing_client

    context.pop()

