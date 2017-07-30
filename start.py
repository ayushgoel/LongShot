import github
import github_token
import repositories


def main():
    g = github.Github(github_token.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        print "Got", g.get_tags_and_releases(repo["owner"], repo["name"], repositories.COUNT)
        print "Yes"


if __name__ == '__main__':
    main()
