import github
import constants
import repositories


def main():
    g = github.Github(constants.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        print "Got", g.getTagsAndReleases(repo["owner"], repo["name"], repositories.COUNT).json()


if __name__ == '__main__':
    main()
