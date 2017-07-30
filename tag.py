
class Tag:
    def __init__(self, data):
        self.version = data["name"]
        self.URL = data["target"]["commitUrl"]

    def flockML(self):
        return '<a href="{1}">{0}</a>'.format(self.version, self.URL)
