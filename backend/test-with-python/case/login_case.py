import pytest
from api.login import login_api


@pytest.mark.parametrize("email, password,response_code", [
    ("demotest@163.com", "123456", 200,)
])
def test_should_login_successfully(email, password, response_code):
    response = login_api(email, password)
    response_body = response.json()
    assert response.status_code == response_code
    assert response_body["user"]["email"] == email


@pytest.mark.parametrize("email, password,response_code", [
    ("another@example.com", "789012", 403)
])
def test_should_login_failed_with_wrong_email(email, password, response_code):
    response = login_api(email, password, check_exception=False)
    response_body = response.json()
    assert response.status_code == response_code
