
class Release:
    def __init__(self, data):
        assert data["prefix"] == "refs/tags/"
        self.version = data["name"]
