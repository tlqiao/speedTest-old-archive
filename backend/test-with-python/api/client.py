import requests
from configs.load_config import get_configs
from jinja2 import Template
from utils.load_csv import read_csv, get_data_file_path


class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def send_request(self, method, endpoint, data=None, check_exception=True):
        url = self.base_url + endpoint
        try:
            response = requests.request(
                method, url, headers=self.headers, json=data)
            response.raise_for_status()  # Check if the response has an error status code
        except Exception as e:
            self.print_request(url, method, data)
            self.print_response(response)
            if(check_exception):
                raise AssertionError(f"API request failed: {str(e)}")

        return response

    def print_request(self, url, method, data):
        print("API request failed:")
        print("URL:", url)
        print("Method:", method)
        print("Headers:", self.headers)
        print("Data:", data)

    def print_response(self, response):
        print("Response:")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.json())


configs = get_configs()
login_user_data = read_csv(get_data_file_path('login_user_data.csv'))
default_client = APIClient(base_url=configs["url"], headers=configs["headers"])


def get_token(email, password):
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
    response = requests.post(
        configs["url"] + "/api/users/login", data=request_body, headers=configs["headers"])
    return "Token " + response.json()["user"]["token"]


def client_with_token(email=login_user_data[1][1], password=login_user_data[1][2]):
    headers = configs["headers"]
    headers["Authorization"] = get_token(email, password)
    service_client_with_token = APIClient(
        base_url=configs["url"], headers=headers)
    return service_client_with_token
