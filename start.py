import github
import github_token
import repositories


def main():
    g = github.Github(github_token.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        print "Got", g.getTagsAndReleases(repo["owner"], repo["name"], repositories.COUNT)


if __name__ == '__main__':
    main()
