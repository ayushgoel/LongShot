import requests

GITHUB_API_URL = "https://api.github.com/graphql"

QUERY = """
query($repository_owner:String!,
      $repository_name: String!,
      $count: Int!) {
  repository(owner: $repository_owner,
             name: $repository_name) {
    
    refs(last: $count, refPrefix:"refs/tags/") {
      nodes {
        name
        target {
          commitUrl
        }
      }
    }
    
    releases(last: $count) {
      nodes {
        tag {
          name
          prefix
        }
      }
    }

  }
}
"""


class Github:
    def __authorization_header(self):
        return "token " + self.token

    def __request_headers(self):
        return {
            'authorization': self.__authorization_header(),
        }

    def __init__(self, token):
        self.token = token

    def __parse_tags_and_releases(self, response):
        repository = response["data"]["repository"]
        tags = repository["refs"]["nodes"]
        releases = repository["releases"]["nodes"]
        return {"tags": tags,
                "releases": releases}

    def get_tags_and_releases(self, repository_owner, repository_name, count):
        payload = {"query": QUERY,
                   "variables": {
                       "repository_owner": repository_owner,
                       "repository_name": repository_name,
                       "count": count
                   }}
        print "Requesting for", repository_name
        response = requests.post(GITHUB_API_URL, json=payload, headers=self.__request_headers())
        print "Got status code for", repository_name, response.status_code
        return self.__parse_tags_and_releases(response.json())
