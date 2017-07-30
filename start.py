import github
import github_token
import repositories
import tagsparser
import flock


def main():
    g = github.Github(github_token.GITHUB_TOKEN)
    for repo in repositories.REPOSITORIES:
        tags, releases = g.get_tags_and_releases(repo["owner"], repo["name"], repositories.COUNT)
        print "Got", tags, releases
        unreleased_tags = tagsparser.find_unreleased_tags(tags, releases)
        flockML = flock.create_flockML_for_tags(repo["owner"], repo["name"], unreleased_tags)
        flock.notify_group_about_missing_release_notes(flockML)


if __name__ == '__main__':
    main()
