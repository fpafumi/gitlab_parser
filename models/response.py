class Response:
    def __init__(self, headers, payload):
        self._headers = headers
        self._payload = payload

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, new_headers):
        self._headers = new_headers

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, new_payload):
        self._payload = new_payload
