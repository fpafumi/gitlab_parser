class Group:
    def __init__(self, id, url):
        self._id = id
        self._url = url

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, new_url):
        self._url = new_url

    def builder_json_to_groups(json):
        return [Group(item['id'], item['web_url']) for item in json]