from models.group import Group
from models.project import Project
from request.my_request import my_request
from configs.config import *

if __name__ == '__main__':
    try:
        print("--- init script ---")
        response_groups = my_request(base_url, params, method)
        if response_groups is None:
            raise Exception("Errore durante la connessione al server gitlab")
        groups = Group.builder_json_to_groups(response_groups.payload)

        for page in range(int(response_groups.headers['X-Total-Pages'])):
            response_groups = my_request(base_url, params, method)
            if response_groups is None:
                raise Exception("Errore durante la connessione al server gitlab")
            groups = Group.builder_json_to_groups(response_groups.payload)

            for group in groups:

                response_projects = my_request(f"{base_url}{group.id}", None, method)

                if response_projects is None or 'projects' not in response_projects.payload:
                    continue

                projects = Project.builder_json_to_project(response_projects.payload['projects'])

                for project in projects:
                    print(f"Sto scrivendo ID: {project.id}, URL: {project.web_url}")
                    with open('urls.txt', 'a') as file:
                        file.write(f"{project.web_url}\n")
            params['page'] = int(params['page']) + 1
    except Exception as e:
        print(f"Ho riscontrato un errore: {e}")
