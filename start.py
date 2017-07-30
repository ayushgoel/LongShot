import github
import github_token
import repositories
import tagsparser


def main():
    g = github.Github(github_token.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        data = g.get_tags_and_releases(repo["owner"], repo["name"], repositories.COUNT)
        print "Got", data
        unreleased_tags = tagsparser.find_unreleased_tags(data["tags"], data["releases"])


if __name__ == '__main__':
    main()
