import requests
import tag
import release

GITHUB_API_URL = "https://api.github.com/graphql"

QUERY = """
query($repository_owner:String!,
      $repository_name: String!,
      $tags_count: Int!,
      $releases_count: Int!,) {
  repository(owner: $repository_owner,
             name: $repository_name) {

    refs(last: $tags_count, refPrefix:"refs/tags/") {
      nodes {
        name
        target {
          commitUrl
        }
      }
    }

    releases(last: $releases_count) {
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
        tags = [tag.Tag(i) for i in repository["refs"]["nodes"]]
        releases = [release.Release(i["tag"]) for i in repository["releases"]["nodes"]]
        return (tags, releases)

    def get_tags_and_releases(self, repository_owner, repository_name, tags_count, releases_count):
        payload = {"query": QUERY,
                   "variables": {
                       "repository_owner": repository_owner,
                       "repository_name": repository_name,
                       "tags_count": tags_count,
                       "releases_count": releases_count
                   }}
        print "Requesting for", repository_name
        response = requests.post(GITHUB_API_URL, json=payload, headers=self.__request_headers())
        print "Got status code for", repository_name, response.status_code
        return self.__parse_tags_and_releases(response.json())
