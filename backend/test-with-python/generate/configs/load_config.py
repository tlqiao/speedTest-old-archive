import json
import os


def get_configs():
    environment = os.environ.get('env') if os.environ.get('env') else "dev"
    file_path = os.path.dirname(os.path.abspath(
        __file__)) + '/config_' + environment + '.json'
    with open(file_path, 'r') as file:
        json_content = file.read()
    data = json.loads(json_content)
    return data
