
class Tag:
    def __init__(self, data):
        self.version = data["name"]
        self.URL = data["target"]["commitUrl"]
