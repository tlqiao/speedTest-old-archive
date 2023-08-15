from flask import Flask, request, send_file
import os
import shutil
import zipfile
import glob


app = Flask(__name__)


@app.route('/generate_project', methods=['GET'])
def generate_project():
    delete_generate_files()
    delete_zip_file()
    project_name = request.args.get('project_name')
    project_folder = create_folder(project_name)
    copy_files(project_folder)
    create_requirements(project_folder)
    file_path, file_name = zip_file(project_name, project_folder)
    return download_file(file_path, file_name)


def create_folder(project_name):
    project_folder = os.path.join(os.getcwd()+'/generate', project_name)
    os.makedirs(project_folder, exist_ok=True)
    print("create folder  {project_folder} successfully")
    return project_folder


# def copy_files(project_folder):
#     existing_folders = ['api', 'case', 'configs', 'data', 'db', 'utils']
#     for folder_name in existing_folders:
#         source_folder_path = os.path.join(os.getcwd(), folder_name)
#         destination_folder_path = os.path.join(project_folder, folder_name)
#         os.makedirs(destination_folder_path)
#         for source_file_name in os.listdir(source_folder_path):
#             print("---source_file_name---" + source_file_name)
#             if source_file_name.endswith('.py') or source_file_name.endswith('.json') or source_file_name.endswith('csv'):
#                 source_file_path = os.path.join(
#                     source_folder_path, source_file_name)
#                 shutil.copy(source_file_path, destination_folder_path)
#     print("copy  files successfully")


def copy_files(project_folder):
    existing_folders = ['api', 'case', 'configs', 'data', 'db', 'utils']
    for folder_name in existing_folders:
        source_folder_path = os.path.join(os.getcwd(), folder_name)
        destination_folder_path = os.path.join(project_folder, folder_name)
        shutil.copytree(source_folder_path, destination_folder_path)
        cache_folder = os.path.join(destination_folder_path, '__pycache__')
        if os.path.exists(cache_folder) and os.path.isdir(cache_folder):
            shutil.rmtree(cache_folder)
    print("copy  files successfully")


def create_requirements(project_folder):
    source_path = os.path.join(os.getcwd(), 'requirements.txt')
    destination_path = os.path.join(project_folder, 'requirements.txt')
    shutil.copyfile(source_path, destination_path)
    print("copy the requirements.txt file successfully")


def zip_file(project_name, project_folder):
    zip_filename = f'{project_name}.zip'
    zip_filepath = os.path.join(os.getcwd(), zip_filename)
    with zipfile.ZipFile(zip_filepath, 'w') as zipf:
        for root, dirs, files in os.walk(project_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(
                    file_path, project_folder))
    return zip_filepath, zip_filename


def download_file(zip_filepath, zip_filename):
    return send_file(zip_filepath, as_attachment=True, attachment_filename=zip_filename)


def delete_generate_files():
    folder_name = 'generate'
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    print("delete generate folder and files in the folder successfully")


def delete_zip_file():
    zip_files = glob.glob(os.path.join('./', '*.zip'))
    if zip_files:
        for zip_file in zip_files:
            os.remove(zip_file)
    print("delete zip files successfully")


if __name__ == '__main__':
    app.run()
