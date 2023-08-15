from jinja2 import Template
from api.client import client_with_token


def add_article(title):
    body_template = '''
        {
            "article": {
                "tagList": [],
                "title": "{{title}}",
                "description": "test summary",
                "body": "this is a test article",
            }
        }
        '''
    request_body = Template(body_template).render(title=title)
    response = client_with_token().send_request(
        "POST", "/api/articles/", data=request_body)
    return response


def get_article(limit=10):
    response = client_with_token().send_request(
        "GET", "/api/articles?limit={limit}&offset=0")
    return response
