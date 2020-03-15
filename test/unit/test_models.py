from app.models import User


def test_new_user(user):
    """test_new_user
    GIVEN a User model
    WHEN a new User is created
    THEN check if the username, email, password_hash, and role fields are defined correctly
    """

    assert user.username == "test_user"
    assert user.email == "test@gmail.com"
    assert user.check_password("test_password") == True
    assert user.check_password("test-password") == False
    assert user.role == 0
