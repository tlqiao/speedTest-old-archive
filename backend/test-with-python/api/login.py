from jinja2 import Template
from api.client import default_client
import json


def login_api(email, password, check_exception=True):

    body_template = '''
        {
            "user": {
                "email": "{{ email }}",
                "password": "{{ password }}"
            }
        }
        '''
    request_body = Template(body_template).render(
        email=email, password=password)

    response = default_client.send_request(
        "POST", "/api/users/login", data=json.loads(request_body), check_exception=check_exception)
    return response
