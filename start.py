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
        text = ""
        for tag in tags:
            if tag.version in unreleased_tags:
                text += "No release for tag {0}, it can be found on {1}".format(tag.version, tag.URL)
        flock.notify_group_about_missing_release_notes(text)


if __name__ == '__main__':
    main()
