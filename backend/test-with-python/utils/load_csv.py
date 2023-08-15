import csv
import os


def get_data_file_path(file_name):
    environment = os.environ.get('env') if os.environ.get('env') else "dev"
    current_folder = os.path.dirname(os.path.abspath(__file__))
    parent_folder = os.path.dirname(current_folder)
    file_path = parent_folder + '/data/' + environment + '/' + file_name
    return file_path


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
