class Project:
    def __init__(self, id, web_url, http_url_to_repo):
        self._id = id
        self._web_url = web_url
        self._http_url_to_repo = http_url_to_repo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def web_url(self):
        return self._web_url

    @web_url.setter
    def web_url(self, new_web_url):
        self._web_url = new_web_url

    @property
    def http_url_to_repo(self):
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, new_http_url_to_repo):
        self._http_url_to_repo = new_http_url_to_repo

    def builder_json_to_project(json):
        return [Project(item['id'], item['web_url'], item['http_url_to_repo']) for item in json]